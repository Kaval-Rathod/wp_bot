# WhatsApp Bot API Server Launcher
Write-Host "Starting WhatsApp Bot App..." -ForegroundColor Green
Write-Host ""

# Change to the project directory where the Python files are located
$projectPath = "C:\kiz\vs_projects\bot"
Set-Location $projectPath

Write-Host "Current directory: $projectPath" -ForegroundColor Cyan

# Check if the Python file exists
if (-not (Test-Path "whatsapp_bot_app.py")) {
    Write-Host "Error: whatsapp_bot_app.py not found!" -ForegroundColor Red
    Write-Host "Make sure this script is in the same folder as whatsapp_bot_app.py" -ForegroundColor Red
    Write-Host ""
    Write-Host "Press any key to exit..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Check if virtual environment exists
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & "venv\Scripts\Activate.ps1"
} else {
    Write-Host "Virtual environment not found, using system Python..." -ForegroundColor Yellow
}

# Run the WhatsApp Bot App
Write-Host "Running WhatsApp Bot App..." -ForegroundColor Green
try {
    python whatsapp_bot_app.py
} catch {
    Write-Host "Error occurred: $_" -ForegroundColor Red
    Write-Host "Press any key to exit..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
} 