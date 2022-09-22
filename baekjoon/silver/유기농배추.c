#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define size 51
int M, N, K;
int map[size][size];
int visited[size][size];

int dh[] = {-1, 1, 0, 0};
int dw[] = {0, 0, -1, 1};
void FloodFill(int h, int w){
    if(h<0 || h>=N || w>=M || w<0)return;
    if(map[h][w] != 1) return;
    if(visited[h][w]) return;

    visited[h][w] = 1;
    for(int i=0; i<4;i++){
        FloodFill(h+dh[i], w+dw[i]);
    }    
}

int Solve(){
    memset(visited, 0, sizeof(visited));
    int cnt = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if (!visited[i][j] && map[i][j]){
                FloodFill(i, j);
                cnt++;
            }
        }
    }
    return cnt;
}

void InputData(){
    int x, y;
    scanf("%d %d %d", &M, &N, &K);
    for(int i=0; i<K; i++){
        scanf("%d %d", &x, &y);
        map[y][x] = 1;
    }
}

int main(){
    int ans = 0;
    int T;
    scanf("%d", &T);

    for(int t=0; t<T; t++){
        memset(map, 0, sizeof(map));        
        InputData();
        ans = Solve();     
        printf("%d\n", ans);           
    }    
    return 0;
}