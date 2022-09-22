#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)1e3)
int N, K;
int A[MAXN+10];
int visited[MAXN+10];

void InputData(){
    scanf("%d %d", &N, &K);
    for(int i=1; i<=N; i++){
        A[i] = i;
    }
}

int main(){
    InputData();
    int sol[MAXN+10];
    
    int cnt = 0;
    int idx = 0; 
    while(cnt < N){ //sol 배열에 cnt == N이 될때까지 값 추가
        for(int i = 0; i<K; i++){
           while(1){
                idx++;
                if (idx > N) idx = 1;
                if (!visited[idx]) break;
           }
        }
        visited[idx] = 1;
        sol[cnt++] = A[idx];        
    }
    
    printf("<");
    for(int i=0; i<N; i++){
        printf("%d", sol[i]);
        if (i<N-1) printf(", ");
    }
    printf(">");
    
    return 0;
}