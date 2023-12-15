<?php


namespace Tests\Feature;

use Tests\TestCase;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\ServerException;
class ApiTest extends TestCase
{   
    private $httpClient;

    protected function setUp(): void
    {
        parent::setUp();
        $this->httpClient = new Client([
            'base_uri' => 'https://selenium-python.readthedocs.io',
            'verify' => false
        ]);
    }
    public function testStatusCodeIs200()
    {
        // Hacer una solicitud a la ruta de índice (puedes usar cURL, Guzzle, etc.)
        $response = $this->httpClient->get('/getting-started.html');
    

        // Verificar si el código de respuesta es 200
        $this->assertEquals(200, $response->getStatusCode());
    }
}
