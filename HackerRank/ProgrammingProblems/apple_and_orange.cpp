#include <iostream>



int main() {


    int s, t, a, b, m, n;
    std::cin >> s >> t >> a >> b >> m >> n;

    int apple_distances[m];
    int orange_distances[n];

    for (unsigned int i = 0; i < m; i++) 
        std::cin >> apple_distances[i];

    for (unsigned int i = 0; i < n; i++) 
        std::cin >> orange_distances[i];


    int apples = 0, oranges = 0;

    for (unsigned i = 0; i < m; i++) {
        int apple_position = apple_distances[i] + a; 
        if (apple_position >= s && apple_position <= t)
            apples++;
    }

    for (unsigned i = 0; i < n; i++) {
        int orange_position = orange_distances[i] + b; 
        if (orange_position >= s && orange_position <= t)
            oranges++;
    }
    std::cout << apples << std::endl << oranges << std::endl;
    

    return 0;
}