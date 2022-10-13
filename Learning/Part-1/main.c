#ifndef F_CPU

#define F_CPU 16000000UL // clock speed is 16MHz

#endif

#include <avr/io.h>     // AVR header
#include <util/delay.h> // delay header
#include "lcd.h"
#include "keypad header.h"
#define KEY_PRT PORTA
#define KEY_DDR DDRA
#define KEY_PIN PINA
#define Fan_ON() PORTD |= (1<<0)
#define Fan_OFF() PORTD &= ~(1<<0)
#define Heater_ON() PORTD |= (1 << 1)
#define Heater_OFF() PORTD &= ~(1 << 1)
#define Fan_ON() PORTD |= (1<<0)
#define Fan_OFF() PORTD &= ~(1<<0)
#define Heater_ON() PORTD |= (1 << 1)
#define Heater_OFF() PORTD &= ~(1 << 1)
int i = 0, j = 0, no = 0,temp2;
int* convert(char* temperature1);
char selecNum();
char temperature1[2];
char personNum();
int selecnumber = 0, personnumber = 0;
void LCD_String(char *str);
void Hincrease();
void Hdecrease();
void LCD_Display_INT_TO_STRING(int value);
int adc_read(char channel)
{
	unsigned int result, x;
	ADMUX = channel;
	ADCSRA = 0x80;
	ADCH = 0x00;
	ADCL = 0x00;
	ADCSRA |= (1 << 6);  //start the conversion
	// wait till conversion is finished
	while ( (ADCSRA & 0x40) != 0 );
	x = ADCL;
	result = ADCH;
	result = result << 8;
	result = result | x;
	return result;
}
int main(void)
{
	unsigned int volt;
	unsigned int temp;
	DDRD |= (1<<0) ;
	DDRD |= (1<<1);
	
 while(1){   
	DDRC = 0xFF;
	volt = adc_read(0);
	volt = volt * 4.88;  //convert into mV
	temp = volt/10;
	LCD_Set();

	LCD_Write_String("  FSS Table 1.0   ");
	_delay_ms(1000);
	//...............................................................................................................................................................................
	do
	{
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("    TIME(FUNK)");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("MENU PRESS");

		selecNum();
		selecnumber = no;
		_delay_ms(1000);
		LCD_cmd(0x01); // clear screen
		LCD_Write_String(" CONFIRM CHOICE ");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("   ");
		_delay_ms(1000);
		do
		{
			LCD_cmd(0x01); // clear screen
			LCD_Write_String("ENTER + RESELECT");
			LCD_cmd(0xC0); // move cursor to the start of 2nd line
			LCD_Write_String("ENTER x CONFIRM");
			char accept = keyfind();
			switch (accept)
			{
				case ('*'):
				i = 1;
				j = 1;
				//...............................................................................................................................................................................
				do
				{
					LCD_cmd(0x01); // clear screen
					LCD_Write_String("   ENTER DATA");
					LCD_cmd(0xC0); // move cursor to the start of 2nd line
					LCD_Write_String("   TYPE");
					if (no == 3)
					{personnumber = no;
					_delay_ms(1000);
					LCD_cmd(0x01); // clear screen 
					LCD_Write_String(" CONFIRM DATA");
					LCD_cmd(0xC0); // move cursor to the start of 2nd line
					LCD_Write_String("   ENTERED");
					_delay_ms(1000);}
					else{personnumber = no;}
					
						
					do
					{
						LCD_cmd(0x01); // clear screen
						LCD_Write_String("ENTER + RESELECT");
						LCD_cmd(0xC0); // move cursor to the start of 2nd line
						LCD_Write_String("ENTER x CONFIRM");
						char accept = keyfind();
						switch (accept)
						{
							case ('*'):
							i = 1;
							j = 1;
							LCD_cmd(0x01); // clear screen
							LCD_Write_String("SETTING........");
							LCD_cmd(0xC0); // move cursor to the start of 2nd line
							_delay_ms(1000);
							LCD_Write_String("ALL SET");
							break;
							case ('+'):
							i = 1;
							j = 0;
							break;
							default:
							i = 0;
						}

					} while (i == 0);

				} while (j == 0);
				//...........................................................................................................................................................................
				break;
				case ('+'):
				i = 1;
				j = 0;
				break;
				default:
				i = 0;
			}

		} while (i == 0);

	} while (j == 0);

	switch (selecnumber)
	{
		case 1:
		DDRC |= 0x08;
		
		PORTC = 0x08;
		_delay_ms(2000);
		break;
		
		case 2:
		DDRC |= 0x08;
		PORTC &= ~(1<<3);
		_delay_ms(2000);
		break;
		case 3:
	   convert(temperature1);
		if (temp>=temp2)
		{
			Fan_ON();
			_delay_ms(1000);
		}else if (temp<=temp2)
		{
			Heater_ON();
			_delay_ms(1000);
		break;
		case 4:
		Fan_OFF();
		Heater_OFF();
		_delay_ms(1000);
		break;
		case 5:
		Hincrease();
		break;
		case 6:
		Hdecrease();
		break;
		case 7:
		DDRD |= 0x08;
		PORTD = 0x08;
		_delay_ms(2000);
		break;
		case 8:
		DDRD |= 0x08;
		PORTD &= ~(1<<3);
		_delay_ms(2000);
		break;
		
	}

	//Countdown coding --------------------------------------------------------

	_delay_ms(1000);
	LCD_cmd(0xC0); // move cursor to the start of 2nd line
	LCD_Write_String("THANK YOU!");
	_delay_ms(1000);
	LCD_cmd(0x01); // clear screen
	LCD_cmd(0x01); // clear screen
	LCD_cmd(0xC0); // move cursor to the start of 2nd line
	LCD_Write_String("   THANK YOU !");
	_delay_ms(1000);
}
}
		}
char selecNum()
{
	char test = keyfind();
	switch (test)
	{
		case ('1'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("UNLOCK SOLENOID");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     LOCK");
		no = 1;
		break;
		case ('2'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("LOCK SOLENOID");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     LOCK");
		no = 2;
		break;
		case ('3'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("     TURN UP ");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     HEAT");
		no = 3;
		break;
		case ('4'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("      TURN DOWN");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     HEAT");
		no = 9;
		break;
		case ('5'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("     INCREASE");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     ELEVATION");
		no = 5;
		break;
		case ('6'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("	DECREASE");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     ELEVATION");
		no = 6;
		break;
		case ('7'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("	TURN ON");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     LIGHT");
		no = 7;
		break;
		case ('8'):
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("   TURN OFF");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     LIGHT");
		no = 8;
		break;
		default:
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("   PLEASE ADD");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     NUMBER");
		_delay_ms(1000);
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("   ADD SELECTION");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("     NUMBER ");
		selecNum();
	}
}
/*char PASS(){
	char test = keyfind();
			LCD_cmd(0x01); // clear screen
			LCD_Write_String("   PLEASE Enter");
			LCD_cmd(0xC0); // move cursor to the start of 2nd line
			LCD_Write_String("PASSWORD");
			_delay_ms(1000);
			PASS();
}*/
char TEMP()
{
	char test = keyfind();
	char temperature[2];
	for (int k=0;k<5; k++)
	{
	switch (test)
	{
		case ('1'):
		temperature[k] = 1;
		break;
		case ('2'):
		temperature[k] = 2;
		break;
		case ('3'):
		temperature[k] = 3;
		break;
		case ('9'):
		temperature[k] = 9;
		break;
		case ('4'):
		temperature[k]= 4;
		break;
		case ('5'):
		temperature[k]= 5;
		break;
		case ('6'):
		temperature[k]= 6;
		break;
		case ('7'):
		temperature[k]= 7;
		break;
		case ('8'):
		temperature[k]= 8;
		break;
		default:
		LCD_cmd(0x01); // clear screen
		LCD_Write_String("   PLEASE Enter");
		LCD_cmd(0xC0); // move cursor to the start of 2nd line
		LCD_Write_String("  TEMPERATURE");
		personNum();
	}
	}
	
	temperature1[2] = temperature[2];
}
int* convert(char* temperature1)
{
	int len=strlen(temperature1),i;
	int *temp1=(int*)malloc(len*sizeof(int));
	for(i=0;i<len;i++)
	temp1[i]=temperature1[i]-48;
	temp2 = temp1;
}
void Hincrease(){
	PORTC |= (1<<PORTC2);
	_delay_ms(100000);
	PORTC &= ~ (1<<PORTC2);
	//_delay_ms(1000);
}

void Hdecrease(){
	PORTC |= (1<<PORTC2);
	_delay_ms(100000);
	PORTC &= ~ (1<<PORTC2);
	//_delay_ms(1000);
}
