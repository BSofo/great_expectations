import unittest
import json

import great_expectations as ge
from great_expectations import render

class TestPageRenderers(unittest.TestCase):

    def test_import(self):
        from great_expectations import render

    def test_prescriptive_expectation_renderer(self):
        results = render.render(
            renderer_class=render.PrescriptiveExpectationPageRenderer,
            expectations=json.load(open('tests/test_fixtures/rendering_fixtures/expectation_suite_3.json'))["expectations"],
        )
        assert results != None

        # with open('./test.html', 'w') as f:
        #     f.write(results)

    def test_descriptive_evr_renderer(self):
        R = render.DescriptiveEvrPageRenderer(
          json.load(open('tests/test_fixtures/rendering_fixtures/evr_suite_3.json'))["results"],
        )
        rendered_page = R.render()
        assert rendered_page != None

        # with open('./test.html', 'w') as f:
        #     f.write(rendered_page)


    def test_full_oobe_flow(sefl):
        # df = ge.read_csv("examples/data/Titanic.csv")
        df = ge.read_csv("examples/data/Meteorite_Landings.csv")
        df.autoinspect(ge.dataset.autoinspect.pseudo_pandas_profiling)
        # df.autoinspect(ge.dataset.autoinspect.columns_exist)
        evrs = df.validate()["results"]
        # print(json.dumps(evrs, indent=2))

        R = render.DescriptiveEvrPageRenderer(evrs)
        rendered_page = R.render()
        assert rendered_page != None

        with open('./test.html', 'w') as f:
            f.write(rendered_page)

class TestSectionRenderers(unittest.TestCase):

    def test_render_modes(sefl):
        df = ge.read_csv("examples/data/Meteorite_Landings.csv")
        df.autoinspect(ge.dataset.autoinspect.pseudo_pandas_profiling)
        expectations_list = df.get_expectations_config()["expectations"]
        # print( json.dumps(expectations_list, indent=2) )

        # evrs = df.validate()["results"]
        # print( json.dumps(evrs, indent=2) )

        R = render.PrescriptiveExpectationColumnSectionRenderer(
            column_name="",
            expectations_list=expectations_list
        )
        rendered_section = R.render()
        assert rendered_section != None
        json.dumps(rendered_section)
        # print( json.dumps(rendered_section, indent=2) )

        rendered_section = R.render('html')
        # print( rendered_section )

        # with open('./test.html', 'w') as f:
        #     f.write(rendered_page)

        assert "<li> must never be missing.</li>" in rendered_section