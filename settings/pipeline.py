# encoding:utf-8
##### PIPELINE ################################################################
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'estilos': {
        'source_filenames': (
            'stylus/prueba.styl',
        ),
        'output_filename': 'css/s.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {}
"""
    'standard': {
        'source_filenames': [
            'js/sample1.coffee',
        ],
        'output_filename': 'js/s.js',
    }
"""

PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)
