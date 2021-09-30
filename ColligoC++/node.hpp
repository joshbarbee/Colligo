#ifndef node
#define node
#endif


#include <stdio.h>
#include <vector>
#include <set>

template<typename T>
class Node {
public: 
	std::vector<Node<T>*> previous;
	std::vector<Node<T>*> next;
	T data;

	Node(T val) {
		data = val;
	}

	void setPrevious(std::vector<Node<T>*>& new_prev);

	void setNext(std::vector<Node<T>*>& new_next);

	void addNext(Node<T>* new_next);

	void addPrev(Node<T>* new_prev);
};

template<typename T>
void Node<T>::setPrevious(std::vector<Node<T>*>& new_prev) {
	this->previous.clear();

	for (Node<T>* node : new_prev) {
		this->previous.push_back(node);
		node->next.push_back(this);
	}
}

template<typename T>
void Node<T>::setNext(std::vector<Node<T>*>& new_next) {
	this->next.clear();

	for (Node<T>* node : new_next) {
		this->next.push_back(node);
		node->previous.push_back(this);
	}
}

template<typename T>
void Node<T>::addNext(Node<T>* new_next) {
	this->next.push_back(new_next);
	new_next->previous.push_back(this);
}

template<typename T>
void Node<T>::addPrev(Node<T>* new_prev) {
	this->previous.push_back(new_prev);
	new_prev->next.push_back(this);
}

