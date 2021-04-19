## Introduction
RSA is public-key cryptosystem which can be used for encryption and digital signatures developed by Ron Rivest, Adi Shamir, and Leonard Adleman. Security is based on complex number factorization problem.

## Subsoil of RSA
![Subsoil of RSA](https://user-images.githubusercontent.com/45511879/115297850-fab28a00-a15c-11eb-98a9-01da2af6a42c.png)


## Correctness Proof of RSA
![Correctness Proof  of RSA](https://user-images.githubusercontent.com/45511879/115297871-00a86b00-a15d-11eb-8852-494bc07763f6.png)

## Preparation of RSA parameters
This process has three steps: generation of private and public key, encryption, decryption
### Key generation
1. Draw dwo random  distinct prime numbers p and q (The best way to increse security if prime numbers have similar bits lenght but with distant values from each other)
2. Compute N = pq 
3. Compute ![image](https://user-images.githubusercontent.com/45511879/115300120-e2903a00-a15f-11eb-9b29-169cfe89074a.png)
4. Draw an integer e such that ![image](https://user-images.githubusercontent.com/45511879/115300412-3ac73c00-a160-11eb-9baa-37e6505e8d6a.png), e and phi(N) must be coprime
5. Designate d from ![image](https://user-images.githubusercontent.com/45511879/115300790-add0b280-a160-11eb-8730-e85238bdc11c.png) (The easiest way is to use Extended Euclides Algorithm - xgcd)
6. Lets define private key - (d, N) which one we keep in secret and public key - (e, N) which we can share.
### Encryption
Let's choose message **m** an integer to encrypt such that ![image](https://user-images.githubusercontent.com/45511879/115302034-4287e000-a162-11eb-85e7-58b03c31b473.png), now we can
use **public key - (e,N)** and this formula where **c** is ciphertext 
<br />
![image](https://user-images.githubusercontent.com/45511879/115302536-d35ebb80-a162-11eb-84fb-0bdb18470705.png)
<br />
Now ciphered message **c** is ready to send.
### Decryption
Let's revover **m** from **c** by using **private key - (d,N)** and this formula
<br />
![image](https://user-images.githubusercontent.com/45511879/115303044-639d0080-a163-11eb-8c61-f232c1bac8b9.png)
<br />
Now we can read the message where **m** is original message

## bibliography
1. Neal Koblitz - A Course in Number Theory and Cryptography
2. https://en.wikipedia.org/wiki/RSA_(cryptosystem)
