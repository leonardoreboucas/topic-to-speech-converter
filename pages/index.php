<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Listing</title>
</head>
<body>
    <h2>List of Files in the Directory</h2>
    <ul>
        <?php
        // Get the list of files in the current directory
        $files = scandir(__DIR__."/audio");

        // Iterate over the files and display them as links
        foreach ($files as $file) {
            // Ignore the '.' and '..' directories
            if ($file != '.' && $file != '..') {
                // Create a link for the file
                echo '<li><a href="audio/' . $file . '">' . $file . '</a></li>';
            }
        }
        ?>
    </ul>
</body>
</html>
