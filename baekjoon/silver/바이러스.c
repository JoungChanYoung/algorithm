#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)1e2)
int N, E; //컴퓨터 수, 엣지 수 
int visited[MAXN+10];
int A[MAXN+10][MAXN+10];
int que[MAXN+10];
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
    return wp==rp;
}

int BFS(){
    int cnt = 0;
    push(1);    
    visited[1] = 1;
    while(!empty()){
        int cur = front(); pop();
        for(int i=1; i<=N; i++){
            if (A[cur][i] && !visited[i]){ //방문 안한 노드이고, 방문할 수 있으면 push 
                visited[i] = 1;
                push(i);                            
                cnt++;         
            }
        }                       
    }
    return cnt;
}

void InputData(){ //input 받고 edge 정리
    int a, b;
    scanf("%d", &N);
    scanf("%d", &E);
    for(int i=1; i<=E; i++){
        scanf("%d %d", &a, &b);
        A[a][b] = 1;
        A[b][a] = 1;
    }
}

int main(){
    int ans = 0;

    InputData();

    ans = BFS();

    printf("%d", ans);
    return 0;
}