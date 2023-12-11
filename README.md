# pucrio-mvp4

Este é um projeto básico (MVP) para estudo e avaliação da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes**.

O projeto tem como objetivo utilizar modelos de predição para identificar se times de hóquei (NHL) devem ganhar ou perder determinada partida a partir de quão agressivo jogou, levando como base:

- Hits -> Quantidade de acertos que os jogadores tiveram em outros jogadores (contatos, empurrões, cortes de contato etc);
- Takeaways -> Quantidade de roubo de discos, seja no mano a mano ou interceptação de passe;
- FaceOffWinPercentage -> Percentual de vitórias em faceoffs. Faceoff é uma disputa de disco parado entre dois jogadores com auxílio do árbitro.

Para mais informações sobre regras da NHL, [acesse aqui](https://www.nhl.com/info/video-rulebook).

O projeto contempla 3 modelos de aprendizado:

- [Decision Tree](https://scikit-learn.org/stable/modules/tree.html)
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [XGB](https://xgboost.readthedocs.io/en/stable/get_started.html)

E também demonstra 2 modelos com precisão abaixo do esperado pelo projeto:

- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [SVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)


## Dependências

Instale as dependências com `pip install -r requirements.txt`

## Rode o projeto

Para rodar o projeto, na raiz execute `python3 -m flask run --host=0.0.0.0 --port=5001`

## Importe o arquivo de dados

Neste repositório há um arquivo de dados para ser utilizado na demonstração em `tests/game_teams_stats.csv`.

O arquivo foi baixado do repositório [Kaggle](https://www.kaggle.com/datasets/martinellis/nhl-game-data).

Utilize esse arquivo por conveniência.

## Rode os testes

O projeto possui apenas 2 testes:

- Certifica de que todos os modelos que estão implementados tem precisão igual ou acima do mínimo esperado;
- Certifica de que determinados modelos conhecidos falham em alcançar a precisão mínima esperada com o dataset fornecido.

Para rodar os testes, na raiz do projeto execute `python3 pytest`

## Alternativamente, utilize o Colab

Você pode rodar os modelos [via Colab aqui](https://github.com/kelvindules/pucrio-mvp4/blob/main/colab.ipynb)
