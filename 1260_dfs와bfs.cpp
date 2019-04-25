#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
vector<int> v[1010];
vector<bool> visit(1010, false);
vector<bool> visit2(1010, false);
queue<int> q;
void dfs(int num){
	if (visit[num])
		return;
	cout << num << " ";
	visit[num] = true;
	for (int i = 0; i < v[num].size(); i++){
		dfs(v[num][i]);
	}
}

void bfs(int num){
	q.push(num);
	while (!q.empty()){
		int tmp = q.front();

		for (int i = 0; i < v[tmp].size(); i++){
			if (visit2[v[tmp][i]])
				continue;
			q.push(v[tmp][i]);
		}
		if (!visit2[tmp])
			cout << tmp << " ";
		visit2[tmp] = true;
		q.pop();
	}
}

int main()
{
	int N, M, start, a, b;
	cin >> N >> M >> start;
	for (int i = 0; i < M; i++){
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	for (int i = 0; i < N; i++){
		sort(v[i].begin(), v[i].end());
	}

	dfs(start);
	cout << endl;
	bfs(start);
	return 0;
}
