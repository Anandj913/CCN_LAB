#include <bits/stdc++.h>
using namespace std;

int find_min_Distance(vector<int>& dist, vector<bool>& sptSet)
{
      
    int min = INT_MAX, min_index;
  
    for (int n = 0; n < dist.size(); n++)
        if (sptSet[n] == false && dist[n] <= min)
        {
            min = dist[n];
            min_index = n;
        }
  
    return min_index;
}
  
void printPath(vector<int>& parent, int j)
{
      
    if (parent[j] == - 1)
        return;
  
    printPath(parent, parent[j]);
  	cout << j+1 << "->";
}
  
void printSolution(vector<int> &dist, vector<int> &parent, int src, int destination_router)
{
	if(src == destination_router)
		return;
	if(dist[destination_router] == INT_MAX)
	{
		cout << "\n  " << src+1 << " -> " << destination_router+1 << " \t Infinity\t\t No path possible";
		return;
	}
    cout << "\n  " << src+1 << " -> " << destination_router+1 << " \t " << dist[destination_router] << "\t\t\t " << src+1 << "->";
    printPath(parent, parent[destination_router]);
    cout << destination_router +1;
}
 
void dijkstra(vector<vector<int> > &graph, int src, int node)
{
      
    vector<int> dist(node, INT_MAX);
	vector<bool> sptSet(node, false);
	vector<int> parent(node, -1);
    
    dist[src] = 0;
  
    for (int count = 0; count < node - 1; count++)
    {
        int u = find_min_Distance(dist, sptSet);
        sptSet[u] = true;
  
        for (int v = 0; v < node; v++)
  
            if (!sptSet[v] && graph[u][v] && dist[u] + graph[u][v] < dist[v])
            {
                parent[v] = u;
                dist[v] = dist[u] + graph[u][v];
            } 
    }
    cout << "\n|---------------------------------------------------------------------------|\n";
    cout << "  Printing shortest path from router " << src +1<< " to every other router\n";
  	cout << "\n  Routers\t Shortest Distance\tRouting Path";
  	for(int i=0; i<node; i++)
  	{
  		printSolution(dist, parent, src, i);
  	}
  	cout << "\n";
  	cout << "\n|---------------------------------------------------------------------------|\n";
}

int main()
{

	int node,s, d, w, src;
	cout << "Enter number of routers in network: ";
	cin >> node;
	vector<vector<int> > graph(node, vector<int>(node, 0));

	cout << "Enter connections of routers as source_router_num destination_router_number weight\n";
	cout << "Enter -1 to end entering\n";
  	cout << "source destination weight\n";

  	do{
  		cin >> s;
  		if(s==-1)
  		{
  			continue;
  		}
  		cin >> d >> w;
  		graph[s-1][d-1] = w;

  	}while(s!=-1);

	cout << "Enter Source router number: ";

	cin >> src;
	cout << "\nRunning Dijkstra Algorithm\n";
	dijkstra(graph, src-1, node);
    return 0;
}