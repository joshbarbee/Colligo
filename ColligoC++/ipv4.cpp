#ifndef node
#define node
#endif

#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <regex>

bool isValidIPV4(std::string ip) {
	if (ip.length() > 15) {
		return false;
	}

	std::regex pattern("(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0- 9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])");
	int arr[4];

	//temp container for substrings
	std::string tString;

	for (int i = 0; i < ip.length(); i++) {
		
	}
}