## 🧱 Full Installation Breakdown for Conjure on Windows (via WSL2)

---

### 🔹 **STEP 0: Open PowerShell as Administrator**
Before anything else, all PowerShell commands were run **with Administrator privileges**.

---

### 🔹 **STEP 1: Install WSL2 & Ubuntu**  
📍 *Tool: PowerShell*

```powershell
wsl --install
```

- This installs **Windows Subsystem for Linux** (WSL2) and **Ubuntu (default)**.
- ✅ **Reboot required** after this step.

---

### 🔹 **STEP 2: Check WSL Status**  
📍 *Tool: PowerShell*

```powershell
wsl --status
```

- You saw that **WSL1 was unsupported** and **WSL2 was the default**, but WSL features weren’t fully enabled yet.

---

### 🔹 **STEP 3: Enable Required Windows Features**  
📍 *Tool: PowerShell (Admin)*

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- ✅ **Reboot required** after this step to apply changes.

---

### 🔹 **STEP 4: Install Ubuntu Manually** (because it wasn’t auto-installed)  
📍 *Tool: PowerShell*

```powershell
wsl --install -d Ubuntu
```

- Downloads and installs Ubuntu (usually 22.04 or later).
- On first launch, Ubuntu prompted you to:
  - Create a UNIX **username**
  - Set a **password**

---

### 🔹 **STEP 5: Open the Ubuntu Terminal**  
📍 *Tool: Start Menu → Ubuntu or run `wsl` in PowerShell*

You’re now inside the **Linux shell**:
```bash
the_rfc@S15N2512GB:~$
```

---

### 🔹 **STEP 6: Install Required Packages in Ubuntu**

#### ✅ 6.1: Update & Install `unzip`  
📍 *Tool: Ubuntu terminal*

```bash
sudo apt update && sudo apt install unzip -y
```

---

### 🔹 **STEP 7: Download and Install Conjure**  
📍 *Tool: Ubuntu terminal*

```bash
wget https://github.com/conjure-cp/conjure/releases/download/v2.5.1/conjure-v2.5.1-linux-with-solvers.zip
unzip conjure-v2.5.1-linux-with-solvers.zip
```

---

### 🔹 **STEP 8: Add Conjure to Your PATH**  
📍 *Tool: Ubuntu terminal*

```bash
echo 'export PATH="$HOME/conjure-v2.5.1-linux-with-solvers:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### 🔹 **STEP 9: Verify Conjure Installation**  
📍 *Tool: Ubuntu terminal*

```bash
conjure --version
```

- Output confirmed: `Conjure version 2.5.1`

---

### 🔹 **STEP 10: Install Java (Required for Savile Row)**  
📍 *Tool: Ubuntu terminal*

```bash
sudo apt install default-jre -y
```

---

### 🔹 **STEP 11: Verify Java Installation**  
📍 *Tool: Ubuntu terminal*

```bash
java -version
```

- Output confirmed: OpenJDK 21.0.6 (✅ Compatible with Savile Row)

---

### 🔹 **STEP 12: Final Verification & PATH Check**

```bash
pwd                    # Should return /home/the_rfc
echo $PATH | grep conjure
```

- ✅ Confirmed Conjure is in the PATH
- ✅ You're in the correct working directory

---

## ✅ You're Now Fully Set Up!

You now have:
- A working **Linux dev environment** via WSL
- Conjure + Savile Row + Minion all configured
- Java ready to run solvers
- Everything available from the Ubuntu terminal