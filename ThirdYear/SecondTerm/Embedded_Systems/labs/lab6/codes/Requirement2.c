/// @author Abdelaziz Salah
/// @author Mahmoud Reda
/// @date 26/3/2023

// example 2
void shift(int seed)
{
    // counter = seed/
    /// for (i = 0 ; i < 4; i++){
    /// delay (500) ms
    /// portD |= counter;
    /// counter <<= 1;
    // }
}

// void seed (int seed) {
//     // put the seed into the ports we want to work on
//     // portD = seed
//     // portE = seed
// }

void main()
{

    // void loop
    while (1)
    {
        int seed1 = 0x1111;
        // seed(seed1);
        shift(seed1);
        int seed2 = 0xEEEE;
        // seed(seed2);
        shift(seed2);
    }
}