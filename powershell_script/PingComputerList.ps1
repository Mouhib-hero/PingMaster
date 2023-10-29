$date = Get-Date
Add-Content -Path "Results\PingResults.txt" "`n--$date--`n"
$ComputersList = @()
$ComputersList = Get-Content IP_addresses\AdresseIP.txt
foreach($Computer in $ComputersList){

   $Ping = Test-Connection -ComputerName $Computer -Count 1 -Quiet -ErrorAction SilentlyContinue 
   if($Ping -eq "True") {
	   Add-Content -Path "Results\PingResults.txt" "$Computer : en ligne"
   }else {
	   Add-Content -Path "Results\PingResults.txt" "$Computer : hors ligne"
   } 
}