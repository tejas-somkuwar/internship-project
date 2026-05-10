#include <iostream>
using namespace std;

// Function to compute GCD
int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to find modular inverse
int modInverse(int e, int phi)
{
    for (int d = 2; d < phi; d++)
    {
        if ((e * d) % phi == 1)
        {
            return d;
        }
    }
    return -1;
}

// Function for modular exponentiation
int modExp(int base, int exp, int mod)
{
    int result = 1;
    base = base % mod;

    while (exp > 0)
    {
        if (exp % 2 == 1)
        {
            result = (result * base) % mod;
        }

        exp = exp / 2;
        base = (base * base) % mod;
    }

    return result;
}

int main()
{
    int m, p, q, e, d, n, phi;

    // Input message
    cout << "Enter Message: ";
    cin >> m;

    // Input prime numbers
    cout << "Enter first prime number: ";
    cin >> p;

    cout << "Enter second prime number: ";
    cin >> q;

    // Calculate n and phi
    n = p * q;
    phi = (p - 1) * (q - 1);

    // Find e
    for (e = 2; e < phi; e++)
    {
        if (gcd(e, phi) == 1)
        {
            break;
        }
    }

    // Find d
    d = modInverse(e, phi);

    if (d == -1)
    {
        cout << "No modular inverse found";
        return 1;
    }

    // Display keys
    cout << "Public Key: (" << e << ", " << n << ")" << endl;
    cout << "Private Key: (" << d << ", " << n << ")" << endl;

    // Encryption
    int c = modExp(m, e, n);
    cout << "Encrypted Message: " << c << endl;

    // Decryption
    int decryptedMessage = modExp(c, d, n);
    cout << "Decrypted Message: " << decryptedMessage << endl;

    return 0;
}
