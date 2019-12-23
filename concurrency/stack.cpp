#include <exception>

struct empty_stack: std::exception
{
    const char* what() const throw();
};

