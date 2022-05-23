#include <bits/stdc++.h>
using namespace std;


struct Edge {
    int source, dest, weight;
};

struct Graph {
  int V;        
  int E;        
  struct Edge* edge;  
};

struct Graph* createGraph(int V, int E) {
  struct Graph* graph = new Graph;
  graph->V = V;  
  graph->E = E;  
  graph->edge = new Edge[E];
  return graph;
}


void printPath(vector<int> &parent, int j)
{
    if (j == -1) {
        return;
    }
    printPath(parent, parent[j]);
    cout << j +1 << "->";
    
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
    cout << "\n  " << src+1 << " -> " << destination_router+1 << " \t " << dist[destination_router] << "\t\t\t ";
    printPath(parent, parent[destination_router]);
    cout << destination_router +1;
}
 
void bellmanFord(struct Graph* graph, int source)
{

    int V = graph->V;
    int E = graph->E;
    struct Edge* edge = graph->edge;
    vector<int> dist(V, INT_MAX);
    dist[source] = 0;
 
    vector<int> parent(V, -1);
 
    int u, v, w, k = V;
    while (--k)
    {
        for (int j = 0; j < E; j++) 
        {
            u = edge[j].source;
            v = edge[j].dest;
            w = edge[j].weight;

            if (dist[u] != INT_MAX && dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
 
    for (int j = 0; j < E; j++) 
    {
        u = edge[j].source;
        v = edge[j].dest;
        w = edge[j].weight;
        if (dist[u] != INT_MAX && dist[u] + w < dist[v])
        {
            cout << "Negative-weight cycle is found!!";
            return;
        }
    }
 
    cout << "\n|---------------------------------------------------------------------------|\n";
    cout << "  Printing shortest path from router " << source +1<< " to every other router\n";
    cout << "\n  Routers\t Shortest Distance\tRouting Path";
    for(int i=0; i<V; i++)
    {
      printSolution(dist, parent, source, i);
    }
    cout << "\n";
    cout << "\n|---------------------------------------------------------------------------|\n";
}
 
int main()
{

  int V, E, s, d, w, src;
  cout << "Enter number of routers in network: ";
  cin >> V;
  cout << "Enter number of connections in network: ";
  cin >> E;
  struct Graph* graph = createGraph(V, E);
  cout << "Enter connections of routers as source_router_num destination_router_number weight\n";
  cout << "source destination weight\n";
  for(int i=0; i<E; i++)
  {
    cin >> s >> d >> w;
    graph->edge[i].source = s-1;
    graph->edge[i].dest = d-1;
    graph->edge[i].weight = w;

  }
  cout << "Enter Source router number: ";
  cin >> src;
  cout << "\nRunning Bellman ford's Algorithm\n";

  bellmanFord(graph, src-1);
 
  return 0;
}