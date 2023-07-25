# Mesa Balanceadora

### Autores: Gabriel Pietroluongo Nascimento, Luiz Gabriel Bandeira e Ribeiro, Otávio Costa Sales

O projeto consiste em um sistema de reconhecimento de imagem e uma mesa acoplada a servo motores. O sistema é capaz de identificar a posição de um objeto (no nosso exemplo, uma bolinha de pingue-pongue laranja) pela cor e movimentar a mesa utilizando os servos para que o objeto não caia da mesa. O projeto foi desenvolvido na disciplina de Projeto Integrado de Computação II, ofertada na Universidade Federal do Espírito Santo.

## Arquitetura
![image](https://github.com/pietroluongo/balance/assets/43349294/beb93d05-fbe2-4139-9596-94e849103573)

Existem ao todo quatro componentes no sistema, dois principais (a ESP e o Computador) e dois secundários (a câmera e os servos).
A câmera serve para fornecer de forma contínua a posição do objeto. Ele envia as imagens (os frames do video) para o computador.
O computador é responsável por receber cada frame do vídeo, identificar todos os pixels da cor selecionada e enviar a média desses pixels para a ESP-32, num formato JSON {x, y}
A ESP cuida do controle PID, responsável por calcular como os servo motores precisam atuar para que o objeto se mantenha equilibrado em cima da mesa.
Os servo motores são responsáveis por movimentar a mesa, fazendo com o que o objeto raramente escorregue para fora.

## Como executar
As informações específicas sobre como rodar cada um dos dois módulos estão disponíveis nas subpastas específicas de cada módulo.
- [ESP](https://github.com/pietroluongo/balance/tree/main/esp)
- [Câmera](https://github.com/pietroluongo/balance/tree/main/camera)

Além disso, os arquivos `.blend` esão disponíveis na pasta [PIC2](https://github.com/pietroluongo/balance/tree/main/PIC2)

# Requisitos
## Requisitos de software
- [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam&hl=en&gl=US) para captar as imagens através do celular e enviá-las para uma rede local
- Python 3 e OpenCV para o código do reconhecimento de imagem
- MQTT para o envio de informações entre o notebook e a ESP
- C++, PlataformIO para o código de controle PID
- Blender para criar os modelos 3d necessários
## Requisitos de hardware
- Câmera
- Um computador para rodar o código de reconhecimento de imagem.
- Um microcontrolador para rodar o código de controle PID.
- Dois servo motores
## Hardware utilizado
- Celular com câmera
- Notebook para rodar o código de reconhecimento de imagem.
- Microcontrolador ESP-32 para controle dos motores
- Servo motor SG-90 (x2)
## Outros requisitos
- Peças impressas em 3D
- Material em MDF para construção da estrutura da mesa
- [Junta Universal 1/4"](https://www.amazon.com.br/Stanley-4-86-011-Junta-Universal-Amarelo/dp/B076VQ5KH9/ref=sxts_rp_s_1_0?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&content-id=amzn1.sym.086bd8c4-d9e4-415a-8862-4106b70dc76c%3Aamzn1.sym.086bd8c4-d9e4-415a-8862-4106b70dc76c&cv_ct_cx=junta%2Buniversal%2B1%2F4&keywords=junta%2Buniversal%2B1%2F4&pd_rd_i=B076VQ5KH9&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1-f0029781-b79b-4b60-9cb0-eeda4dea34d6&th=1)

## Mais mídias
![image](https://github.com/pietroluongo/balance/assets/43349294/c123020a-f4a4-493c-8a12-96991951b30e)

Peças impressas em impressora 3D para suporte dos servo motores e da mesa

![image](https://github.com/pietroluongo/balance/assets/43349294/0fdba27f-b602-4e26-8371-64e474c67444)
Imagem de referência de como ficou a montagem

![image](https://github.com/pietroluongo/balance/assets/43349294/fcf4db3a-02c2-4582-90ab-7de8ae224bff)

Modelo 3D do servo motor utilizado para a montagem do suporte

![image](https://github.com/pietroluongo/balance/assets/43349294/d92692a4-f4bb-4588-84ae-9649c07b7e8f)

Primeiro protótipo funcional

[Video da mesa em ação](https://www.youtube.com/shorts/Di8BZghZs8M)

# Referências
Vídeos no Youtube:
- [Ball Balancing PID System](https://www.youtube.com/watch?v=7Jw8m4pbTYI&t=2s)
- [PID Balance+Ball | full explanation & tuning](https://www.youtube.com/watch?v=JFTJ2SS4xyA)
- [Acrome Ball Balancing Table](https://www.youtube.com/watch?v=tPr6-Rh0m-8)
