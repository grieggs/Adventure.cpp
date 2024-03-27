1. ssh into your llama server
2.  start llama.cpp
    `./server -m ~/llama2-70b.Q5_K_M.gguf -c 2048 --threads 15 -ngl 80`
3. forward port `ssh -L 8080:localhost:8080 username@host`
3. 