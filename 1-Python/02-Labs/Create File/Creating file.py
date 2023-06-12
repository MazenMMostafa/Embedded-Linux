f1=open("UART_Program.c","w")
f1.write('#include "UART_Interface.h" ')
f1.close

f1=open("UART_Interface.h","w")
f1.write('#ifndef UART_INTERFACE_H_ \n #define UART_INTERFACE_H_ \n#include "UART_Private.h"\n#include "UART_Config.h" #endif')
f1.close

f1=open("UART_Register.h","w")
f1.write('#ifndef UART_REGISTER_H_ \n #define UART_REGISTER_H_ \n#endif')
f1.close

f1=open("UART_Private.h","w")
f1.write('#ifndef UART_PRIVATE_H_\n#define UART_PRIVATE_H_\n#include "UART_Register.h"\n#endif')
f1.close

f1=open("UART_Config.h","w")
f1.write('#ifndef UART_CONFIG_H_ \n #define UART_CONFIG_H_ \n#include "UART_Register.h" #endif')
f1.close
