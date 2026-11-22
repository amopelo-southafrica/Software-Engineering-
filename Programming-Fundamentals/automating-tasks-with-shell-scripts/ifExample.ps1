if (Test-Path -Path new_folder){ 
    New-Item -Path if_folder -ItemType Directory
    Write-Output "if_folder has been created"
}

if (Test-Path -Path if_folder){
    New-Item -Path hyperiondev -ItemType Directory
    Write-Output "hyperiondev has been created"
} else {
     New-Item -Path new-projects -ItemType Directory
     Write-Output "new-projects has been created"
}
