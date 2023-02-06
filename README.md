# nearby-restaurants
API that allow users to find nearly restaurants in real time (just as Google Maps does now)

# Installation (before execution)

Give executing right
```bash
chmod u+x search
```

Create Python virtual env
```bash
make venv
```

Activate virtual env
```bash
source venv/bin/activate
```

Install all required dependencies
```bash
make deps
```

# Execution
Execute all tests
```bash
make test
```

Execute search
```bash
./search latitude=48.8319929 longitude=2.3245488 radius=100
```

```shell
name:Le Severo,longitude:2.3245488,latitude:48.8319929,distance:0.0
name:Félicie,longitude:2.3247172,latitude:48.832418,distance:48.85
name:Chez Toni,longitude:2.3246523,latitude:48.8321391,distance:17.94
name:Sushi House,longitude:2.3247528,latitude:48.8319258,distance:16.69
name:Au P'tit Zinc,longitude:2.3247495,latitude:48.8323129,distance:38.5
name:Le Saut du Crapaud,longitude:2.3242762,latitude:48.8315833,distance:49.72
name:Mikopüy,longitude:2.3247313,latitude:48.8318918,distance:17.46
name:Lida,longitude:2.324098,latitude:48.8313102,distance:82.77
```

Clean virtual env
```bash
make clean
```
