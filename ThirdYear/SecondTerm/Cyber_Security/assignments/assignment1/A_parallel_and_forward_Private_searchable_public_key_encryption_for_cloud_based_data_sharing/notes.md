# Parallel and forward private searchable public key encryption (PFP-SPE)
* The problem which the paper try to solve is:
  * At the time when the paper was first published, the current schemes which existed, was suffering from lack of parallelism and forward security.
* what is the parallelis: 
  * it is the ability to search for the encrypted messages using multiThreaded machines.
* what is the forward security:
  * Forward security, also known as forward secrecy, is a property of cryptographic protocols that ensures that the compromise of long-term secret keys does not allow an attacker to decrypt past communication sessions that were previously encrypted using those keys.

  *   In other words, forward security means that even if an attacker gains access to a secret key used to encrypt past communication, they will not be able to use that key to decrypt past communications.

  *   Forward security is important because it limits the amount of information an attacker can gain from a compromised key. If forward security is not employed, an attacker who compromises a long-term secret key can decrypt all communication that was encrypted using that key, potentially compromising a large amount of sensitive information.

  *   Forward security is often achieved through the use of ephemeral keys, which are temporary keys that are generated for each individual communication session. Ephemeral keys are never used again after the session is completed, so even if they are compromised, they cannot be used to decrypt past sessions.
  
  *   mn el akher keda, de btdmn en lw 7d e5trk el private key bta3k by2drsh eno yfok tshfer 7agat etshfrt abl keda khlas. 
  *   t2oley ezay da mmkn ye7sl, a2olak bkol bassata el session keys el kona bntklm 3leha fe chapter 14, enta lw 7d edr ye3rf el session key, hwa mmkn yefok el messages el bt7sl fl communication da bs, lakn ba2y el 7agat el adema mby2drsh eno yefokha gher lw b2a m3ah el master key baa. 
  
* tb hwa el klam da by722a2oh mn gher ma yedf3o dareba keda y3ny? mafesh fl donya haga mlhash pros and cons. 
* el dareba el bydf3oha hya enohom byst5dmo storage zyada shwayaa. -> more cost. 

### Pros
1. Parallelism on encryption search
2. Forward Security (Forward Secrecy)
3. Similar Search efficiency as the symmetric encryption
4. No key distribution problem
   
### Cons
1. Higher storage cost
2. Complexity of implementation: Implementing PFP-SPE correctly can be challenging, and small implementation errors or weaknesses in the system design can potentially compromise the security of the data.

### Searchable encryption
* it means that we can search for the data without needing to decrypt it.
  
* el 7elw fe keda enk bt7awl t7afz 3la el security bta3t el system bta3ak w kman t7afez en el data tkon available toul el w2t. 

### broad Categories of searchable encryption
* symmetric searchable encryption (SSE)
  * this requires that all users share the same key to generate the ciphertext and the search keywords. 
  * this causes a problem of key distribution.
  * but it has high computational performance. 
  * and low storage cost.
* searchable    public key encryption (SPE):
  * this solves the drawbacks of the symmetric encryption.
  * but it is impractical because it can be attacked easily either by guessing keywords or file injection. 
  * moreover its performance is very low and impractical to be applied.
* most of SPE schemes that are developed to solve the problem of that scheme still could not resist the injection attacks. 

* An injection attack is a process where an attacker injects or infects your web application with malicious code to retrieve your personal information or compromise your system. The attacker tricks your system into thinking that the command was initiated by you and it blindly processes the command. 

### purpose of the paper
* this paper tries to develop a parallel SPE scheme. 

### Contributions of the paper
1. introducing a new variant searchable public-key encryption scheme called PFP-SPE which achieves parallelism and forward security.
2. giving a concrete construction of PFP-SPE and present
a formal security proof under the computable bilinear
Dife-Hellman assumption.
3. Testing this scheme on a real-world dataset and validating its performance, and getting a conclusion that the scheme is practical and efficient.

### Cyclic groups 
