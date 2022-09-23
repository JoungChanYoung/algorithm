#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)3e2)

int l;
int cur_w, cur_h;
int tar_w, tar_h;
int visited[MAXN+10][MAXN+10];

struct ST{
    int h, w, t;
};
struct ST que[MAXN*MAXN+10]; //que사이즈 넉넉하게
int wp, rp;
int dh[] = {-1, -2, -2, -1, 1, 2, 2, 1};
int dw[] = {-2, -1, 1, 2, 2, 1, -1, -2};
void push(int h, int w, int t){
    if(h<0 || h>=l || w<0 || w>=l) return;    
    if(visited[h][w]) return;
    visited[h][w] = 1;
    que[wp].h = h; que[wp].w = w; que[wp].t = t;
    wp++;
}
void pop(){
    rp++;
}
struct ST front(){
    return que[rp];
}
int empty(){
    return wp == rp;
}

int BFS(){
    push(cur_h, cur_w, 0);
    while(!empty()){
        struct ST cur = front(); pop();
        if (cur.h == tar_h && cur.w == tar_w) {
            return cur.t;            
        }
        for(int i=0; i<8; i++){
            push(cur.h+dh[i], cur.w+dw[i], cur.t+1);      
        }
    }    
    return 0;
}

int Solve(){
    int sol = 0;
    memset(visited, 0, sizeof(visited));
    wp = rp = 0;
    sol = BFS();
    return sol;
}

void InputData(){
    scanf("%d", &l);
    scanf("%d %d", &cur_h, &cur_w);
    scanf("%d %d", &tar_h, &tar_w);
}

int main(){
    int T;
    scanf("%d", &T);
    for (int t=0; t<T;t++){
        InputData();
        printf("%d\n", Solve());
    }
    
    return 0;
}