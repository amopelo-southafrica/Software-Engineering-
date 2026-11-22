$menu = Read-Host "
Which folder do you want to add subfolders to?
1 - $mainfoldername1
2 - $mainfoldername2
3 - $mainfoldername3
"

if ($menu -eq "1") {

    $sub1 = Read-Host "Enter name of first subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername1\$sub1"

    $sub2 = Read-Host "Enter name of second subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername1\$sub2"

    $sub3 = Read-Host "Enter name of third subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername1\$sub3"

    Remove-Item $mainfoldername2 -Recurse -Force
    Remove-Item $mainfoldername3 -Recurse -Force
}

elseif ($menu -eq "2") {

    $sub1 = Read-Host "Enter name of first subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername2\$sub1"

    $sub2 = Read-Host "Enter name of second subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername2\$sub2"

    $sub3 = Read-Host "Enter name of third subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername2\$sub3"

    Remove-Item $mainfoldername1 -Recurse -Force
    Remove-Item $mainfoldername3 -Recurse -Force
}

elseif ($menu -eq "3") {

    $sub1 = Read-Host "Enter name of first subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername3\$sub1"

    $sub2 = Read-Host "Enter name of second subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername3\$sub2"

    $sub3 = Read-Host "Enter name of third subfolder"
    New-Item -ItemType Directory -Path "$mainfoldername3\$sub3"

    Remove-Item $mainfoldername1 -Recurse -Force
    Remove-Item $mainfoldername2 -Recurse -Force
}

else {
    Write-Output "Invalid choice. Please enter 1, 2, or 3."
}


