#include <iostream>
using namespace std;

template<class t>
class stackList
{
public:
    class node
    {
    public:

        node() {}
        node(t* dat) { data = dat; }

        node* next = nullptr;
        t* data = nullptr;
    };

    void push(node* n)
    {
        if (n == nullptr) return;

        size++;

        if (head == nullptr)
        {
            head = tail = n;
            return;
        }

        tail->next = n;
        tail = n;
    }

    node* pop_back()
    {
        if (size == 0) return nullptr;

        size--;

        node* n = head;

        if (size == 0)
        {
            head = tail = nullptr;
            return n;
        }
        while (n->next != tail)
            n = n->next;
        n->next = nullptr;
        node* e = tail;
        tail = n;
        return e;
    }

    node* pop_front()
    {
        if (size == 0) return nullptr;

        size--;

        node* n = head;
        head = head->next;
        return n;
    }

    node* get_head() { return head; }

    node* get_at(int idx)
    {
        if (idx >= size) return nullptr;

        node* n = head;
        for (int i = 0; i < idx; i++)
        {
            n = n->next;
        }

        return n;
    }

    int get_size() { return size; }

    void clear()
    {
        while (head != nullptr)
        {
            node* n = head;
            head = head->next;
            if (n != nullptr)
                delete n;
        }
        tail = nullptr;
    }

    bool contains(t* val)
    {
        //cout << "searching list ";
        //print(false);
        //cout << "for value " << *val << endl;

        if (size == 0 || *head->data == *val) return true;

        node* n = head;
        while (n != nullptr)
        {
            if (*n->data == *val)
            {
                //cout << "contains value: " << *val << endl;
                return true;
            }
            n = n->next;
        }

        return false;
    }

    void print(bool newline = true)
    {
        node* n = head;
        while (n != nullptr)
        {
            cout << *n->data << ' ';
            n = n->next;
        }
        if(newline)
            cout << endl;
    }

    ~stackList()
    {
        clear();
    }

private:
    node* head = nullptr;
    node* tail = nullptr;
    int size = 0;
};

class graph
{
public:
    stackList<int> verts = stackList<int>();
    stackList<int> edges = stackList<int>();

    void addVert(int num = 1)
    {
        for (int i = 0; i < num; i++)
            verts.push(new stackList<int>::node(new int(verts.get_size())));
    }

    void addEdge(int from, int to)
    {
        edges.push(new stackList<int>::node(new int(from)));
        edges.push(new stackList<int>::node(new int(to)));
    }

    void breadthFirst() //01234567
    {
        stackList<int> stack = stackList<int>();
        stackList<int> visited = stackList<int>();

        int v = *verts.get_at(0)->data;
        cout << v << endl;
        visited.push(new stackList<int>::node(new int(v)));

        while (true)
        {/*
            cout << "visited: ";
            visited.print();*/
            for (int i = 0; i < edges.get_size() - 1; i += 2)
            {
                int* edge1 = edges.get_at(i)->data;
                int* edge2 = edges.get_at(i + 1)->data;

                int* adj = nullptr;

                if (*edge1 == v && !visited.contains(edge2))
                    adj = edge2;
                else if (*edge2 == v && !visited.contains(edge1))
                    adj = edge1;

                if (adj != nullptr)
                {
                    stack.push(new stackList<int>::node(adj));
                }
            }

            if (stack.get_size() == 0) return;

            //cout << "stack: ";
            //stack.print();

            v = *stack.pop_front()->data;
            if (!visited.contains(&v))
            {
                cout << v << endl;
                visited.push(new stackList<int>::node(new int(v)));
            }

        };
    }

    void depthFirst() //01475263
    {
        stackList<int> stack = stackList<int>();
        stackList<int> visited = stackList<int>();

        int v = *verts.get_at(0)->data;
        cout << v << endl;
        visited.push(new stackList<int>::node(new int(v)));
        stack.push(new stackList<int>::node(new int(v)));

        while (true)
        {
            bool changedNode = false;
            for (int i = 0; i < edges.get_size() - 1; i += 2)
            {
                int* edge1 = edges.get_at(i)->data;
                int* edge2 = edges.get_at(i + 1)->data;

                int* adj = nullptr;

                if (*edge1 == v && !visited.contains(edge2))
                    adj = edge2;
                else if (*edge2 == v && !visited.contains(edge1))
                    adj = edge1;

                if (v == 2)
                    cout << "";

                if (adj != nullptr)
                {
                    changedNode = true;
                    cout << *adj << endl;
                    visited.push(new stackList<int>::node(adj));
                    stack.push(new stackList<int>::node(adj));
                    v = *adj;
                    break;
                }
            }

            if (!changedNode)
            {
                if (stack.get_size() == 0) return;
                v = *stack.pop_back()->data;
            }
        }
    }
};

int main()
{
    cout << "graph structure:\n   0\n / | \\ \n 1 2 3\n | | |\n 4 5 6\n \\ | /\n   7" << endl;


    graph g = graph();
    g.addVert(8);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);

    g.addEdge(1, 4);

    g.addEdge(2, 5);

    g.addEdge(3, 6);

    g.addEdge(4, 7);
    g.addEdge(5, 7);
    g.addEdge(6, 7);

    cout << "Breadth first" << endl;

    g.breadthFirst();

    cout << "\nDepth first" << endl;

    g.depthFirst();
};