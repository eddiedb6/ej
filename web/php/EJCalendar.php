<?php

function EJAddCalendarEvent(&$calendarParams) {
    $aid = "aidAddCalendarEvent";
    return EJExecuteWithAuthentication($aid, $calendarParams, function () use ($aid, &$calendarParams) {
        if (EJInsertCalendarEvent($calendarParams)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJIsCalendarEventHappenThisMonth($currentYear, $currentMonth, $eventDatetime, $repeat) {
    $time = explode("-", $eventDatetime);
    $eventYear = intval($time[0]);
    $eventMonth = intval($time[1]);

    if ($repeat <= 0) {
        return ($currentYear == $eventYear) && ($currentMonth == $eventMonth);
    }

    $eventTotalMonth = $eventYear * 12 + $eventMonth;
    $currentTotalMonth = $currentYear * 12 + $currentMonth;
    return (($currentTotalMonth - $eventTotalMonth) % $repeat) == 0;
}

function EJGetCalendarEvent(&$calendarParams) {
    $aid = "aidCalendarEvent";
    return EJExecuteWithAuthentication($aid, $calendarParams, function () use ($aid, &$calendarParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $monthStr = $calendarParams[W3GetAPIParamIndex($aid, "month") + $paramOffset];

        $time = explode("-", $monthStr);
        $currentYear = intval($time[0]);
        $currentMonth = intval($time[1]);
        $nextMonth = $currentMonth + 1;
        $nextYear = $currentYear;
        if ($nextMonth == 13) {
            $nextMonth = 1;
            $nextYear = $currentYear + 1;
        }

        $sql = "select " .
             "calendar.Datetime as datetime, calendar.Name as name, calendar.Note as note, calendar.RepeatMonth as repeatmonth" .
             " from " .
             "calendar" .
             " where " .
             "calendar.Datetime < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
             " order by calendar.Datetime asc";
        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $currentYear, $currentMonth, $aid) {
            $apiDef = W3GetAPIDef($aid);
            $columns = $apiDef[w3ApiResult][w3ApiResultData];

            if (!EJIsCalendarEventHappenThisMonth($currentYear, $currentMonth, $row["datetime"], $row["repeatmonth"])) {
                return;
            }
        
            $result .= "{";
            foreach ($columns as $value) {
                $resultForColumn = $row[$value[w3ApiDataValue]];
                $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
            }
            $result = rtrim($result, ",") . "},";
        });
        $result = rtrim($result, ",") . "]}";

        return $result;
    });
}

?>
