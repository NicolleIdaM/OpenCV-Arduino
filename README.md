# OpenCV Arduino Motion Detector

Projeto simples que usa Python, OpenCV e comunicacao serial para detectar rostos pela webcam e enviar um sinal para um Arduino.

Quando um rosto e detectado, o script envia `1` pela porta serial. Quando nenhum rosto e detectado, envia `0`. No Arduino, esses valores podem ser usados para ligar/desligar um LED, acionar um servo, controlar um rele ou qualquer outro componente.

## Technologies

- Python
- OpenCV
- Arduino Software
- pyserial

## Como Funciona

O arquivo [Face.py](./Face.py) faz o seguinte:

1. Conecta ao Arduino pela porta serial.
2. Abre a webcam do computador.
3. Usa o classificador Haar Cascade do OpenCV para detectar rostos.
4. Mostra a imagem da camera com um retangulo ao redor do rosto detectado.
5. Envia dados para o Arduino:
   - `1` quando detectar rosto.
   - `0` quando nao detectar rosto.
6. Encerra o programa ao pressionar a tecla `e`.

## Requisitos

- Python 3 instalado.
- Arduino conectado ao computador.
- Webcam funcionando.
- Bibliotecas Python:
  - `opencv-python`
  - `pyserial`

## Instalacao

Instale as dependencias com:

```bash
pip install opencv-python pyserial
```

## Configuracao

No arquivo [Face.py](./Face.py), confira se a porta serial esta correta:

```python
port = 'COM3'
```

Se o Arduino estiver em outra porta, altere `COM3` para a porta correspondente.

No Windows, voce pode verificar a porta pela IDE do Arduino em:

```text
Ferramentas > Porta
```

## Como Executar

Com o Arduino conectado e a webcam disponivel, execute:

```bash
python Face.py
```

Para fechar o programa, pressione:

```text
e
```

## Exemplo de Codigo para Arduino

Este exemplo liga um LED no pino 13 quando um rosto e detectado:

```cpp
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);
    }
  }
}
```

## Observacoes

- A taxa serial usada no Python e no Arduino deve ser a mesma: `9600`.
- Se aparecer erro de conexao, verifique se a porta serial esta correta.
- Feche a Serial Monitor da IDE do Arduino antes de rodar o script Python, pois a porta serial pode ficar ocupada.
- O reconhecimento depende da iluminacao, posicao do rosto e qualidade da camera.

## Estrutura do Projeto

```text
.
├─ Face.py
└─ README.md
```

## Links

