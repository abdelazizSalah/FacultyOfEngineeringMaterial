# Notes
1. this chapter is depending on the digital security. 
2. aham haga fl security hya el trust. 
3. bn7dd men el mada el resala, w mdaha emta w tare5ha kam. 
4. lazm ykon fe 3rd party, 34an yeb2a shahed 3la el by7sl w m7dsh yenkr da. 
5. lazm temdy 3la el resala bl private key bta3k. 
6. 34an atmn enk shoft el resala, lazm terg3haly tany w enta baa mady 3leha enta kman. 
7. shoghl el mobile heta soghyara mn el business -> focus on something more important. 
8. btmdy 3la el resaala w b3den temdy 3la el etnen. 
9. D-H -> diff hellman. 
10. El-gamal digital signature. 
    1.  use the private key for encryption.
    2.  use public key for decryption. 
    3.  by3ml hash ll message -> m
    4.  bn5tar k b7es enha tb2a asghar mn (q-1)
    5.  bn7sb temp key = S1 = a^k mod q
    6.  q is a large prime number. 
    7.  compute K^(-1) which is the inverse of K (mod q-1)
    8.  compute the value S2
11. report about the closure of a set <->
12. el hwar latef 0-> zaker baa. 
13. Schnorr Digital signature. 
    1.  choose suitable prime numbers -> p,q
    2.  choose a such that a^q = 1 mod p
    3.  (a,p,q) are global parameters 
    4.  V = a^-Sa -> inverse of a(Sa) 
    5.  (x||y) -> concatinate x with y. 
14. fe algorithms bt2dr enha tgeb large prime numbers, mmkn yewsl 7agmo l 160 bits number. 
15. r is independent on the algorithm, that is why he compare with it. 
16. 