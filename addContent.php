<?php
// Connect to the database
$conn = new mysqli("localhost", "root", "", "gp");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check for AJAX request
if (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    // Handle form submission
    if (isset($_POST['ContentTitle'], $_POST['ContentType'], $_FILES['FileUpload'])) {
        // Validate and sanitize data (implementation omitted for brevity)

        // Prepare file upload
        $target_dir = "uploads/";  // Adjust the upload directory as needed
        $target_file = $target_dir . basename($_FILES["FileUpload"]["name"]);
        $file_type = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

        // Validate file type (implementation omitted)

        // Move the uploaded file
        if (move_uploaded_file($_FILES["FileUpload"]["tmp_name"], $target_file)) {
            // Insert content into the database
            $stmt = $conn->prepare("INSERT INTO content (title, type, file_path) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $_POST['ContentTitle'], $_POST['ContentType'], $target_file);
            if ($stmt->execute()) {
                echo "Content added successfully";
            } else {
                echo "Error adding content: " . $stmt->error;
            }
            $stmt->close();
        } else {
            echo "Error uploading file";
        }
    } else {
        echo "Invalid request";
    }
    $conn->close();
    exit;  // Prevent further script execution
}
?>