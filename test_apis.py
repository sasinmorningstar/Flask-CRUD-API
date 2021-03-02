# -*- coding: utf-8 -*-

import unittest
# import os
import json

from app import create_app, db

class SongTestCase(unittest.TestCase):
    ''' This class represents the song table test cases '''

    def setUp(self):
        '''Define test variables and initialize app.'''

        self.app = create_app()
        self.client = self.app.test_client
        self.song = {'name': 'Smooth Criminal', 'duration': '710s'}

        # binds the app to current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_song_insertion(self):
        '''Testing whether the api can insert a song record (POST request)'''
        post = self.client().post('/Song/', json=self.song)
        self.assertEqual(post.status_code, 201)
        # self.assertIn('Smooth Criminal', post.json.get('name'))



    # def test_get_all_songs(self):
    #     '''Testing whether the api can fetch all the songs (GET request)'''

    #     post = self.client().post('/Song/', data=self.song)
    #     self.assertEqual(post.status_code, 201)

    #     get = self.client().get('/Song/')
    #     self.assertEqual(get.status_code, 200)




    def test_get_song_by_id(self):
        '''Testing whether the api can fetch a song by id.'''
        post = self.client().post('/Song/', json=self.song)
        self.assertEqual(post.status_code, 201)

        result_in_json = json.loads(post.data.decode('utf-8').replace("'", "\""))

        get = self.client().get('/Song/{}'.format(result_in_json['id']))
        self.assertEqual(get.status_code, 200)


    def test_update_song(self):
        '''Testing whether the api can edit an existing song data (PUT request).'''
        post = self.client().post('/Song/', json=self.song)
        self.assertEqual(post.status_code, 201)

        put = self.client().put('/Song/1', json={'name':'Smooth Criminal'})
        self.assertEqual(put.status_code, 200)
        # get = self.client().get('/Song/1')

        # self.assertIn({'name':'Smooth Criminal', 'duration':'800s'}, str(get.data))


    def test_delete_song(self):
        '''Testing whether the api can delete an existing song data (DELETE request).'''

        post = self.client().post('/Song/', json=self.song)
        self.assertEqual(post.status_code, 201)

        delete = self.client().delete('/Song/1')
        self.assertEqual(delete.status_code, 200)

        # Testing to see if the song data still exists, ideally the request should return a 404 status code
        # get = self.client().get('/Song/1')
        # self.assertEqual(get.status_code, 404)



    def tearDown(self):
        '''teardown all initialized variables'''

        with self.app.app_context():
            # drop all tables

            db.session.remove()
            db.drop_all()



# Make the tests conveniently executable
if __name__=='__main__':
    unittest.main()
