## Introduction
RSA is public-key cryptosystem which can be used for encryption and digital signatures developed by Ron Rivest, Adi Shamir, and Leonard Adleman. Security is based on complex number factorization problem.

## Subsoil of RSA
![Subsoil of RSA](https://user-images.githubusercontent.com/45511879/115297850-fab28a00-a15c-11eb-98a9-01da2af6a42c.png)


## Correctness Proof of RSA
![Correctness Proof  of RSA](https://user-images.githubusercontent.com/45511879/115297871-00a86b00-a15d-11eb-8852-494bc07763f6.png)

## Preparation of RSA parameters
This process has three steps: generation of private and public key, encryption, decryption
### Key generation
1. Draw dwo random  distinct prime numbers p and q (The best way to increse security if prime numbers have similar bits length but with distant values from each other)
2. Compute N = pq 
3. Compute ![image](https://user-images.githubusercontent.com/45511879/115300120-e2903a00-a15f-11eb-9b29-169cfe89074a.png)
4. Draw an integer e such that ![image](https://user-images.githubusercontent.com/45511879/115300412-3ac73c00-a160-11eb-9baa-37e6505e8d6a.png), e and phi(N) must be coprime
5. Designate d from ![image](https://user-images.githubusercontent.com/45511879/115300790-add0b280-a160-11eb-8730-e85238bdc11c.png) (The easiest way is to use Extended Euclides Algorithm - xgcd)
6. Lets define private key - (d, N) which one we keep in secret and public key - (e, N) which we can share.
### Encryption
Let's choose message **m** an integer to encrypt such that ![image](https://user-images.githubusercontent.com/45511879/115302034-4287e000-a162-11eb-85e7-58b03c31b473.png), now we can
use **public key - (e,N)** and this formula where **c** is ciphertext <br />
![image](https://user-images.githubusercontent.com/45511879/115302536-d35ebb80-a162-11eb-84fb-0bdb18470705.png)<br />
Now ciphered message **c** is ready to send.
### Decryption
Let's revover **m** from **c** by using **private key - (d,N)** and this formula<br />
![image](https://user-images.githubusercontent.com/45511879/115303044-639d0080-a163-11eb-8c61-f232c1bac8b9.png)<br />
Now we can read the message where **m** is original message
## Security of keys
NIST recommends 2048-bits keys(the size of the modulus N ) for RSA since 2015 and it will remain secure until 2030.Below is a summary of two tables to comparable strengths for Algorithms from NIST publication<br />
![image](https://user-images.githubusercontent.com/45511879/115381340-c29a5e00-a1d3-11eb-8f61-5bd277350f1f.png)<br />
![image](https://user-images.githubusercontent.com/45511879/115381762-2d4b9980-a1d4-11eb-9fd8-f62900239d4a.png)<br />
## Run time analysis and statement of results 
Using the functions of the emulator_rsa, I created a test module that illustrates the time needed to compute key generation, encryption and decryption with a size module N in bits.<br />
![image](https://user-images.githubusercontent.com/45511879/115383471-2c1b6c00-a1d6-11eb-8fad-7941c00fa21e.png)![image](https://user-images.githubusercontent.com/45511879/115383502-36d60100-a1d6-11eb-831d-64f48afbfc91.png)<br />
Summary of result in the table. For each bits length the numer of tests is 100<br />
![image](https://user-images.githubusercontent.com/45511879/115400169-401c9900-a1e9-11eb-92f9-17177db817bb.png)
## Sample output
![image](https://user-images.githubusercontent.com/45511879/115404774-eec2d880-a1ed-11eb-9c22-887b278d2d23.png)


## bibliography
1. Neal Koblitz - A Course in Number Theory and Cryptography
2. https://en.wikipedia.org/wiki/RSA_(cryptosystem)
3. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-57p1r3.pdf
