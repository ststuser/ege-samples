#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;

int main()
{
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    for (int i = 35000000; i < 40000000; ++i)
    {
        int count = 0;
        int sqrtI = round(sqrt(i));
        for (int j = 1; j <= sqrtI; ++j)
        {
            if (i % j == 0) {
                if (j % 2 == 1) {
                    ++count;
                }
                int k = div(i, j).quot;
                if (k % 2 == 1 && j != k) {
                    ++count;
                }
            }
            if (count > 5) {
                break;
            }
        }
        if (count == 5){
            cout << i << endl;
        }
    }
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << "Elapsed Time is " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << " ms" << std::endl;
    cout << endl;
}