#include <iostream>
using namespace std;

class bTreeNode
{

const static int m = 3;
public:
	int** keys = new int*[2 * m - 1]();
	bTreeNode** children = new bTreeNode*[2 * m]();

	bool isLeaf()	//check if the bTreeNode has any children
	{
		for (int i = 0; i < 2 * m; i++)
			if (children[i] != nullptr) return false;
		return true;
	}

	bool isFull()
	{
		if (keys[2 * m - 2] != nullptr) return true;	//keys will always be ordered so if the last key is not null, then the bTreeNode is full
		return false;
	}

	void split()
	{
		if (!isFull() || !isLeaf()) return;

		bTreeNode* left = new bTreeNode();
		bTreeNode* right = new bTreeNode();
		int* median = keys[m - 1];

		keys[m - 1] = nullptr;

		for (int i = 0; i < m - 1; i++)	//left node
		{
			left->keys[i] = keys[i];
			left->children[i] = children[i];
			children[i] = nullptr;
			keys[i] = nullptr;
		}

		left->children[m - 1] = children[m - 1];
		children[m - 1] = nullptr;

		for (int i = m; i < 2 * m - 1; i++)	//right node
		{
			right->keys[i - m] = keys[i];
			right->children[i - m] = children[i];
			children[i] = nullptr;
			keys[i] = nullptr;
		}

		left->children[m - 1] = children[2 * m - 1];
		children[2 * m - 1] = nullptr;

		keys[0] = median;

		children[0] = left;
		children[1] = right;
	}

	void shift(int idx = 0)	//shift elements after idx to the right
	{
		if (keys[2 * m - 2] != nullptr) return; //can't shift further
		for (int i = 2 * m - 1; i > idx; i--)
		{
			keys[i] = keys[i - 1];
		}
		keys[idx] = nullptr;
	}

	void insert(int val)
	{
		if (isFull())
		{
			split();
			if (val < *keys[0])
			{
				children[0]->insert(val);
				return;
			}
			children[1]->insert(val);
			return;
		}

		for (int i = 0; i < 2 * m - 1; i++)
		{
			if (keys[i] == nullptr)	//we've reached the end, put the value here
			{
				keys[i] = new int(val);
				return;
			}

			if (*keys[i] < val && keys[i + 1] == nullptr)	//we've reached the end, put the value here
			{
				keys[i + 1] = new int(val);
				return;
			}

			if ( (i == 0 && *keys[0] > val)) //put the value at the beginning
			{
				shift(0);
				keys[0] = new int(val);
				return;
			}

			else if ((*keys[i] < val && val < *keys[i + 1])) //put the value in between two keys
			{
				shift(i + 1);
				keys[i + 1] = new int(val);
				return;
			}
		}
	}

	void traverse()
	{
		for (int i = 0; i < 2 * m - 1; i++)
		{
			if (children[i] != nullptr) children[i]->traverse();
			if (keys[i] != nullptr) cout << *keys[i] << ' ';
		}

		if (children[2 * m - 1] != nullptr) children[2 * m - 1]->traverse();
	}
};

int main()
{
	bTreeNode tree = bTreeNode();

	for (int i = 1; i <= 8; i++)
	{
		tree.insert(i);
		cout << "insert: " << i << endl;
	}

	cout << "b tree traversal:" << endl;
	tree.traverse();
  cout << endl;
}