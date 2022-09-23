#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)1e3)

int N, M, V;
int map[MAXN+10][MAXN+10];
int visited[MAXN+10];

int que[MAXN*MAXN+10];
int wp, rp;
void push(int n){
    que[wp++] = n;
}
void pop(){
    rp++;
}
int front(){
    return que[rp];
}
int empty(){
    return rp==wp;
}

void BFS(){
    push(V);
    while(!empty()){
        int cur = front(); pop();                
        if (visited[cur]) {
            continue;            
        }
        printf("%d ", cur);
        visited[cur] = 1;    
        for(int i=1; i<=N; i++){
            if(map[cur][i]){
                push(i);                           
            }            
        }        
    }    
}
void DFS(int n){
    if (visited[n]) return;
    visited[n] = 1;
    printf("%d ", n);
    for(int i=1; i<=N; i++){
        if (map[n][i])
            DFS(i);
    }            
}

void InputData(){
    int a, b;
    scanf("%d %d %d", &N, &M, &V);
    for(int i=0; i<M; i++){
        scanf("%d %d", &a, &b);
        map[a][b] = 1;
        map[b][a] = 1;
    }
}


int main(){
    InputData();
    
    DFS(V);    
    memset(visited, 0, sizeof(visited));
    printf("\n");
    BFS();
    return 0;
}