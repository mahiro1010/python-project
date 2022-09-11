"""
how to execute
# pyhonファイル自体の実行例（今回非推奨）
python __main__.py

# pythonプロジェクト(module)の実行例（今回推奨）
python -m myproject
"""

if __name__ == '__main__':
    from .cli import main
    main()