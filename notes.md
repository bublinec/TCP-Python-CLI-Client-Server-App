# Netoworking basics
- project to practise networking basics (sockets, threads, cleient server communication)

**processess**  - program running in the backgound (application/OS program)
                - share the CPU - each app has it for few milisec, they queue
                - processes change turn so quickly it gives us the feeling they all run in the same time - like animation effect
                - more cores - more resources

**thread**  - branch of execution
            - sometimes our program doesn't run in a single execution - has more threads of execution (async code)
            - processor is divided into mulitple sections to process mulitple threads
            - critical code is locked when one thread executes it, to avoid conflict of running same chunk of code by more threads
            - so there are multiple processes (programs) running in our machine and each process has multiple threads (branches of executrion) 
            - EX: browser execution - one thread is fetching a new page, another thread is rendering current page

------------------------
Side Notes:
- ptyhon is dynamically typed, meaning we don't specify the type of variable and we can change it implicitly by reassinging the variable, or conversion
- python is strongly typed, meaning that we cannot for example add string and int, or pass wrong type to a function as in JS
- other dynamically typed languages: JS (without TS), PHP, Perl, Ruby