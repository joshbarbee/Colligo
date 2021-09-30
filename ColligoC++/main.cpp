#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>

template<typename T>
class Node {
private:
	T data;
	static std::set<Node<T>*> visits;
public: 
	std::vector<Node<T>*> previous;
	std::vector<Node<T>*> next;

	Node(T val) {
		data = val;
	}

	void set_previous(std::vector<Node<T>*>& new_prev);

	void set_next(std::vector<Node<T>*>& new_next);

	void add_next(Node<T>* new_next);

	void add_prev(Node<T>* new_prev);

	void shorten_paths();
};

template<typename T>
std::set<Node<T>*> Node<T>::visits = {};

template<typename T>
void Node<T>::set_previous(std::vector<Node<T>*>& new_prev) {
	this->previous.clear();

	for (Node<T>* node : new_prev) {
		this->previous.push_back(node);
		node->next.push_back(this);
	}
}

template<typename T>
void Node<T>::set_next(std::vector<Node<T>*>& new_next) {
	this->next.clear();

	for (Node<T>* node : new_next) {
		this->next.push_back(node);
		node->previous.push_back(this);
	}
}

template<typename T>
void Node<T>::add_next(Node<T>* new_next) {
	this->next.push_back(new_next);
	new_next->previous.push_back(this);
}

template<typename T>
void Node<T>::add_prev(Node<T>* new_prev) {
	this->previous.push_back(new_prev);
	new_prev->next.push_back(this);
}

template<typename T>
void Node<T>::shorten_paths() {
	visits.insert(this);

	int prev_size = this->previous.size();
	int next_size = this->next.size();

	if (prev_size == 1 && next_size == 1) {
		Node<T>* node_prev = this->previous.front();
		Node<T>* node_next = this->next.front();

		node_prev->add_next(node_next);
		return;
	}

	if (prev_size > 0) {
		for (Node<T>* node : this->previous) {
			if (visits.count(node) > 0) {
				node->shorten_paths();
			}
		}
	}

	if (next_size > 0) {
		for (Node<T>* node : this->next) {
			if (visits.count(node) > 0) {
				node->shorten_paths();
			}
		}
	}
}

int main() {
	Node<int> n1 = 5;
	Node<int> n2 = 3;
	Node<int> n3 = 3;

	Node<int> zero = 0;

	zero.add_next(&n1);
	zero.add_prev(&n2);
	n2.add_prev(&n3);

	zero.shorten_paths();
}
