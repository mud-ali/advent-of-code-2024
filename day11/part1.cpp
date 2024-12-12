#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

int main() {

    ifstream file("input.txt");
    vector<long long> v;
    int num;

    while (file >> num) {
        v.push_back(num);
    }

    file.close();

    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;

    for (int run=0;run<25;run++) {
        for (int i=0;i<v.size();i++) {
            string as_string = to_string(v[i]);

            if (v[i] == 0) {
                v[i] = 1;
            } else if (as_string.size() % 2 == 0) {
                string left_half = as_string.substr(0, (as_string.size() / 2));
                v.insert(v.begin() + i, stoll(left_half));
                i++;
                v[i] = stoll(as_string.substr(as_string.size() / 2, as_string.size() / 2));
            } else {
                v[i] *= 2024;
            }
        }
    }

    cout << v.size() << endl;

    return 0;
}