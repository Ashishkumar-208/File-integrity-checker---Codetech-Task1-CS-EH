1.File Integrity Checker project

A Python-based File Integrity Checker that monitors changes in files by calculating and comparing cryptographic hash values.  
This project is developed as part of CODTECH Internship – Task 1.

2.Project Overview

File Integrity is a critical concept in Cybersecurity.  
This tool ensures that files are not modified without authorization by generating and comparing **SHA-256 hash values.

If even a single character in a file is changed, the hash value will change, and the tool will immediately detect it.

3.Objectives

- Monitor files for unauthorized modifications  
- Ensure file integrity using cryptographic hashing  
- Learn real-world security monitoring concepts  
- Build a CLI-based cybersecurity tool using Python  

4.Technologies Used

- Python 3
- hashlib– for SHA-256 hash generation  
- os– for file handling and validation  
- json– for storing and loading hash values  

5.Project Structure

<img width="553" height="186" alt="image" src="https://github.com/user-attachments/assets/981d3d7d-debb-4103-9cbe-7c8c08b89c01" />

6.How It Works

1. User provides the file path via command line  
2. The program calculates the file’s SHA-256 hash  
3. Hash is stored as a baseline (first run)  
4. On subsequent runs, the hash is recalculated  
5. Old hash and new hash are compared  
6. The program reports whether the file is **SAFE or MODIFIED

7.How to Run the Project (Parrot OS / Linux)

1.Clone the Repository
 bash
 https://github.com/Ashishkumar-208/File-integrity-checker---Codetech-Task1-CS-EH

2️.Run the Script
 bash
 python3 checker.py

3️.Provide File Path
 text
 files/test.txt
 
<img width="1597" height="335" alt="Screenshot 2026-02-05 155642" src="https://github.com/user-attachments/assets/4d633f3c-b3a4-49c9-b997-1085de581131" />

#Example Output
 First Run:
✅ File added for monitoring.
🔐 Hash stored successfully.

#After File Modification:
🔴 WARNING!
File has been MODIFIED.

8.Why SHA-256?

  1.Cryptographically secure
  2.Widely used in cybersecurity
  3.Any small change results in a completely different hash

8.Real-World Use Cases

  1.Cybersecurity monitoring systems
  2.Malware detection
  3.SOC (Security Operations Center) tools
  4.Server file protection
  5.Digital forensics

9.Learning Outcome

  1.Understanding of file integrity concepts
  2.Hands-on experience with cryptographic hashing
  3.Practical use of Python in cybersecurity
  4.Exposure to CLI-based security tools

10.Conclusion

This project demonstrates a practical implementation of file integrity monitoring using Python.
It follows industry-standard practices and can be extended further for real-time monitoring and alerting systems.

👤 Author
Ashish Kumar
|| Cybersecurity Intern ||
Python | Linux | Security Tools


