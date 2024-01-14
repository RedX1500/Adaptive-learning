<?php
if ($_FILES['FileUpload']) {
    $fileName = $_FILES['FileUpload']['name'];
    $fileTmpName = $_FILES['FileUpload']['tmp_name'];
    $fileSize = $_FILES['FileUpload']['size'];
    $fileError = $_FILES['FileUpload']['error'];
    $fileType = $_FILES['FileUpload']['type'];

    // Print file details for testing
    echo "File Name: $fileName<br>";
    echo "File Size: $fileSize bytes<br>";
    echo "File Type: $fileType<br>";

    // Upload file to a directory
    $uploadDir = 'uploads/';
    $targetFile = $uploadDir . basename($fileName);

    if (move_uploaded_file($fileTmpName, $targetFile)) {
        echo "File uploaded successfully.";
    } else {
        echo "Error uploading file.";
    }
} else {
    echo "FileUpload key not found.";
}
?>
