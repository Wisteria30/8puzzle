#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
using namespace std;

int findIdxZero(string &crt) {
    for (int i = 0; i < crt.size(); i++) {
        if (crt[i] == '0') {
            return i;
        }
    }
    cout << "Error: '0' is not found." << endl;
    exit(1);
}

int solve(string &S, string &G) {
    int dx[] = {-3, 3, -1, 1};
    unordered_map<string, int> log;

    S.push_back(char(findIdxZero(S) + '0'));
    G.push_back(char(findIdxZero(G) + '0'));
    log[S] = 1;
    queue<string> q;
    q.push(S);
    while (!q.empty()) {
        string crt = q.front();
        q.pop();
        int idxZero = crt[9] - '0';
        for (int i = 0; i < 4; i++) {
            int nextIdxZero = idxZero + dx[i];
            if (i == 2 && idxZero % 3 == 0) continue;
            if (i == 3 && idxZero % 3 == 2) continue;
            if (nextIdxZero < 0 || 8 < nextIdxZero) continue;
            string next = crt;
            swap(next[idxZero], next[nextIdxZero]);
            next[9] = (char)(nextIdxZero + '0');
            if (log[next] == 0) {
                log[next] = log[crt] + 1;
                q.push(next);
            }
            if (log[G] > 0) {
                return log[G];
            }
        }
    }
    return -1;
}

int main(void) {
    string S;
    string G;
    for (int i = 0; i < 9; i++) {
        char tmp;
        cin >> tmp;
        S.push_back(tmp);
    }
    for (int i = 0; i < 9; i++) {
        char tmp;
        cin >> tmp;
        G.push_back(tmp);
    }
    cout << solve(S, G) << endl;
}
