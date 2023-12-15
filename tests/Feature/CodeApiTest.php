<?php

namespace Tests\Feature;

use Tests\TestCase;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\ServerException;

class CodeApiTest extends TestCase
{
    private $httpClient;

    protected function setUp(): void
    {
        parent::setUp();

        $this->httpClient = new Client([
            'base_uri' => 'http://127.0.0.1:8000/',
            'verify' => false,
        ]);
    }

    public function testSeedUserAndLogin()
    {
        try {
            $userSeedResponse = $this->httpClient->post('register', [
                'json' => [
                    // Datos de usuario de prueba
                    'name'=> 'testname',
                    'email' => 'testuser',
                    'password' => 'testpassword',
                    'password_confirmation' => 'testpassword',
                ],
            ]);

            // Verificar si la semilla del usuario tuvo éxito (código 201 creado)
            $this->assertEquals(201, $userSeedResponse->getStatusCode());

            // Extraer el ID de usuario de la respuesta, si es necesario
            $userId = json_decode($userSeedResponse->getBody(), true)['user_id'];

            // Verificar el inicio de sesión del usuario sembrado
            $loginResponse = $this->httpClient->post('login', [
                'json' => [
                    'email' => 'testuser',
                    'password' => 'testpassword',
                ],
            ]);

            // Verificar el código de respuesta para la verificación de inicio de sesión
            $this->assertEquals(200, $loginResponse->getStatusCode());

        } catch (ServerException $e) {
            // Capturar excepciones de servidor, si es necesario
            $this->fail("Error en la solicitud: " . $e->getMessage());
        }
    }
}
