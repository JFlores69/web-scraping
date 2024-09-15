<?php
// Verifica si el formulario fue enviado y si el valor 'dni' está presente
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['dni'])) {
        // Recoge el valor enviado desde el formulario
        $dni = $_POST['dni'];

        // Escapa el DNI para evitar problemas de seguridad
        $dni = escapeshellarg($dni);

        // Ejecuta el script de Python y pasa el DNI como argumento
        $command = escapeshellcmd("python test_selenium.py $dni");
        $output = shell_exec($command);///

        // Muestra el resultado devuelto por Python
        echo "<h1>Resultado de la búsqueda:</h1>";
        echo "<pre>$output</pre>";
    } else {
        echo "DNI no encontrado.";
    }
} else {
    echo "No se ha enviado ningún formulario.";
}
?>

<?php
//muestra de version de python
$output = shell_exec('python --version 2>&1');
echo "<pre>$output</pre>";
?>
