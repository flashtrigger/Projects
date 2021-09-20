#include <iostream>
using namespace std;

class AVLTree
{
public:
	class node
	{
	public:
		node(int val, node* prnt) { value = val; left = right = nullptr; parent = prnt; }

		int value;
		node* left;
		node* right;
		node* parent; //we have this so we can travel upwards

		node* insert(int val)
		{
			if (val == value) return nullptr;

			if (val < value)	//left
			{
				if (left == nullptr)	//create new node
				{
					left = new node(val, this);
					return left;
				}

				//otherwise insert into left node
				return left->insert(val);
			}

			//right
			if (right == nullptr)
			{
				right = new node(val, this);
				return right;
			}

			return right->insert(val);
		}

		void rotate(bool clockwise)
		{
			if (parent == nullptr) return;

			if (clockwise)
			{
				if (left == nullptr || left->left == nullptr || right || left->right) return; //invalid

				node* n3 = this;
				node* n2 = left;

				n2->parent = parent;
				if (parent->left == this) parent->left = n2;
				else parent->right = n2;

				parent = n2;

				n2->right = n3;
				left = nullptr;

				return;
			}

			if (!clockwise)
			{
				if (right == nullptr || right->right == nullptr || left || right->left) return; //invalid

				node* n3 = this;
				node* n2 = right;

				n2->parent = parent;
				if (parent->left == this) parent->left = n2;
				else parent->right = n2;

				parent = n2;

				n2->left = n3;
				right = nullptr;

				return;
			}
		}

		void traverse()
		{
			if (left != nullptr)
				left->traverse();
			if (right != nullptr) right->traverse();

			cout << value << ' ';
		}

		void destroy()
		{
			if (left != nullptr)
				left->destroy();
			if (right != nullptr) right->destroy();

			delete this;
		}
	};

	node* root = nullptr;

	void insert(int val)
	{
		if (root == nullptr)
		{
			root = new node(val, nullptr);
			return;
		}

		node* w = root->insert(val);	//standard binary tree insertion
		if (w == nullptr) return;

		//travel upward and see if we have to balance, and if we do, then rotate appropriately
		if (w->parent != nullptr && w->parent->left == w && w->parent->parent != nullptr && w->parent->parent->left == w->parent && w->parent->right == nullptr && w->parent->parent->right == nullptr)
		{
			w->parent->parent->rotate(true);
			return;
		}
		if (w->parent != nullptr && w->parent->right == w && w->parent->parent != nullptr && w->parent->parent->right == w->parent && w->parent->left == nullptr && w->parent->parent->left == nullptr)
		{
			w->parent->parent->rotate(false);
			return;
		}
	}

	~AVLTree()
	{
		if (root != nullptr) root->destroy();
	}
};

int main()
{
	AVLTree tree = AVLTree();

	for (int i = 5; i <= 10; i++)
	{
		cout << "Inserting " << i << endl;
		tree.insert(i);
	}
	for (int i = 0; i < 5; i++)
	{
		cout << "Inserting " << i << endl;
		tree.insert(i);
	}
	cout << "Traversal: ";
	tree.root->traverse();
}