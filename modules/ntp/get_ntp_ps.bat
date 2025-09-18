@echo off
echo Запрос времени с NTP-сервера...

powershell -Command "$ntpServer = 'pool.ntp.org'; $client = New-Object System.Net.Sockets.UdpClient; $client.Connect($ntpServer, 123); $data = [byte[]]::new(48); $data[0] = 0x1B; $client.Send($data, $data.Length) | Out-Null; $response = $client.Receive([ref]$null); $client.Close(); $seconds = [BitConverter]::ToUInt32($response[43..40], 0) - 2208988800; $utcTime = [DateTimeOffset]::FromUnixTimeSeconds($seconds).DateTime; Write-Host 'NTP время (UTC):' $utcTime.ToString('yyyy-MM-dd HH:mm:ss'); Write-Host 'Локальное время:' $utcTime.ToLocalTime().ToString('yyyy-MM-dd HH:mm:ss')"

pause