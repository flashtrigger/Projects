#include <iostream>
#include <string.h>
#include <algorithm>
#include <list>
using namespace std;
  

class Graph
{
    int num_vertices;    
    list<int> *adjacent;  
  public:
    //constructor
    Graph(int V){ 
      num_vertices = V;  
      adjacent = new list<int>[V]; 
    }

    //destructor
    ~Graph(){ 
      delete [] adjacent;  
    }
    
    //add a new edge to the graph
    void new_edge(int point, int point2) {
      adjacent[point].push_back(point2); adjacent[point2].push_back(point);
    }

    //printer
    void print_tour(){
    int temp = 0;
    for (int i = 0; i < num_vertices; i++)
        if (adjacent[i].size() & 1){   
          temp = i; break;  
        }
    print_tour_extra(temp);
    cout << endl;
    }

    //the function containing the meat for the printer
    void print_tour_extra(int start){
    
      list<int>::iterator itr;
      for (itr = adjacent[start].begin(); itr != adjacent[start].end(); ++itr){
        int temp = *itr;
        if (temp != -1 && validity(start, temp)){
              cout << start << "->" << temp << "  ";
              delete_edge(start, temp);
              print_tour_extra(temp);
          }
      }
    }
    //return true if adjacent vertex of v is the only adjacent vertex
    //or if there are multiple adjacents and edge v-av is not a bridge
    bool validity(int point, int point2){
      
      int count = 0;  
      list<int>::iterator itr;
      for (itr = adjacent[point].begin(); itr != adjacent[point].end(); ++itr)
        if (*itr != -1){
          count++;
        }
      if (count == 1)
        return true;

      bool visited[num_vertices];
      memset(visited, false, num_vertices);
      int count1 = counter(point, visited);
      
      
      delete_edge(point, point2);
      memset(visited, false, num_vertices);
      int count2 = counter(point, visited);
      
      new_edge(point, point2);
      
      return (count1 > count2)? false: true;
    }
    void delete_edge(int point, int point2){
      
      list<int>::iterator itr = find(adjacent[point].begin(), adjacent[point].end(), point2);
      *itr = -1;
      
      
      list<int>::iterator itr2 = find(adjacent[point2].begin(), adjacent[point2].end(), point);
      *itr2 = -1;
    }

    int counter(int y, bool visited[]){
    
      visited[y] = true;